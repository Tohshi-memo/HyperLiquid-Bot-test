# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T15:07:31.282834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.7207` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.3855` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `0.383` n `228`; crypto_major avg `0.5273` n `8`; equity avg `0.2691` n `88`; fx avg `-0.0155` n `6`; index avg `0.0093` n `25`; metal avg `-0.0483` n `20`; unknown avg `-0.0114` n `763`
- 1h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.9066` n `228`; crypto_major avg `0.9696` n `8`; equity avg `-0.3768` n `88`; fx avg `-0.0157` n `6`; index avg `-0.1107` n `25`; metal avg `-0.1724` n `20`; unknown avg `0.4607` n `763`
- 4h: commodity avg `-0.2231` n `12`; crypto_alt avg `1.6599` n `228`; crypto_major avg `2.1624` n `8`; equity avg `-0.5583` n `88`; fx avg `-0.0788` n `6`; index avg `-0.1987` n `25`; metal avg `0.8747` n `20`; unknown avg `0.3925` n `763`
- 24h: commodity avg `-0.7527` n `12`; crypto_alt avg `2.452` n `228`; crypto_major avg `2.4068` n `8`; equity avg `0.1174` n `88`; fx avg `-0.0225` n `6`; index avg `-0.3352` n `25`; metal avg `0.277` n `20`; unknown avg `0.4358` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
