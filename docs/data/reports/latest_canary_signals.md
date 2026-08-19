# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T05:07:24.768444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `0.0833` n `230`; crypto_major avg `0.054` n `8`; equity avg `0.2183` n `120`; fx avg `0.001` n `6`; index avg `0.0623` n `25`; metal avg `-0.0145` n `20`; unknown avg `0.2154` n `789`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.046` n `230`; crypto_major avg `0.055` n `8`; equity avg `-0.0718` n `120`; fx avg `-0.0111` n `6`; index avg `0.0056` n `25`; metal avg `-0.0911` n `20`; unknown avg `-0.0539` n `789`
- 4h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0674` n `230`; crypto_major avg `-0.1309` n `8`; equity avg `-0.2109` n `120`; fx avg `-0.0977` n `6`; index avg `-0.1163` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.1888` n `789`
- 24h: commodity avg `0.2551` n `12`; crypto_alt avg `0.4653` n `230`; crypto_major avg `0.1892` n `8`; equity avg `-3.2611` n `120`; fx avg `-0.1712` n `6`; index avg `-0.5183` n `25`; metal avg `-0.6196` n `20`; unknown avg `-0.2316` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
