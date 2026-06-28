# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T19:22:28.186333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.014` n `228`; crypto_major avg `-0.1026` n `8`; equity avg `-0.0065` n `88`; fx avg `-0.0285` n `6`; index avg `0.002` n `23`; metal avg `0.0004` n `20`; unknown avg `-0.1026` n `764`
- 1h: commodity avg `0.0132` n `12`; crypto_alt avg `-0.1329` n `228`; crypto_major avg `-0.2415` n `8`; equity avg `-0.0613` n `88`; fx avg `-0.0336` n `6`; index avg `-0.0242` n `23`; metal avg `0.0064` n `20`; unknown avg `0.029` n `764`
- 4h: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.9594` n `228`; crypto_major avg `-0.8916` n `8`; equity avg `-0.127` n `88`; fx avg `-0.0537` n `6`; index avg `-0.0402` n `23`; metal avg `0.0107` n `20`; unknown avg `-0.4867` n `764`
- 24h: commodity avg `0.3361` n `12`; crypto_alt avg `-0.7723` n `228`; crypto_major avg `-1.4017` n `8`; equity avg `0.0109` n `88`; fx avg `-0.0574` n `6`; index avg `-0.0412` n `23`; metal avg `-0.0148` n `20`; unknown avg `14.8131` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
