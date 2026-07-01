# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T16:52:29.104448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4836` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9108` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8865` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.287` n `228`; crypto_major avg `-0.2507` n `8`; equity avg `-0.2143` n `88`; fx avg `0.0038` n `6`; index avg `-0.0436` n `25`; metal avg `-0.0991` n `20`; unknown avg `-0.0013` n `763`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.2717` n `228`; crypto_major avg `-0.251` n `8`; equity avg `-0.0562` n `88`; fx avg `0.004` n `6`; index avg `-0.0386` n `25`; metal avg `-0.0915` n `20`; unknown avg `0.4431` n `763`
- 4h: commodity avg `-0.0463` n `12`; crypto_alt avg `1.8324` n `228`; crypto_major avg `2.4373` n `8`; equity avg `0.5508` n `88`; fx avg `-0.0378` n `6`; index avg `-0.1421` n `25`; metal avg `0.5265` n `20`; unknown avg `1.3267` n `763`
- 24h: commodity avg `-0.6388` n `12`; crypto_alt avg `2.0148` n `228`; crypto_major avg `1.9646` n `8`; equity avg `-0.4528` n `88`; fx avg `-0.0099` n `6`; index avg `-0.4356` n `25`; metal avg `0.2437` n `20`; unknown avg `0.5626` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
