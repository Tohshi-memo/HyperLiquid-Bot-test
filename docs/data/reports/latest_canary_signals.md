# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T02:37:28.364808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.201` n `230`; crypto_major avg `0.2285` n `8`; equity avg `0.0996` n `107`; fx avg `0.0293` n `6`; index avg `0.0374` n `25`; metal avg `0.0272` n `20`; unknown avg `0.019` n `780`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `0.3414` n `230`; crypto_major avg `0.3687` n `8`; equity avg `0.2126` n `107`; fx avg `0.0385` n `6`; index avg `0.0737` n `25`; metal avg `0.0581` n `20`; unknown avg `-0.1391` n `780`
- 4h: commodity avg `0.2405` n `12`; crypto_alt avg `0.3667` n `230`; crypto_major avg `0.5391` n `8`; equity avg `-0.2417` n `107`; fx avg `0.0002` n `6`; index avg `-0.0105` n `25`; metal avg `0.1644` n `20`; unknown avg `-0.2976` n `780`
- 24h: commodity avg `0.2071` n `12`; crypto_alt avg `1.165` n `230`; crypto_major avg `1.0446` n `8`; equity avg `1.3747` n `107`; fx avg `0.0342` n `6`; index avg `0.1325` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.2462` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
