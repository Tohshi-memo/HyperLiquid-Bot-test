# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T23:37:24.389754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `13`; crypto_alt avg `0.1744` n `235`; crypto_major avg `0.1089` n `8`; equity avg `0.0116` n `150`; fx avg `0.0078` n `6`; index avg `0.0049` n `26`; metal avg `0.0108` n `20`; unknown avg `-0.1281` n `1077`
- 1h: commodity avg `-0.0719` n `13`; crypto_alt avg `0.4565` n `235`; crypto_major avg `0.2356` n `8`; equity avg `0.0878` n `150`; fx avg `0.01` n `6`; index avg `0.0172` n `26`; metal avg `0.0547` n `20`; unknown avg `0.4106` n `1075`
- 4h: commodity avg `0.1189` n `13`; crypto_alt avg `1.018` n `235`; crypto_major avg `0.166` n `8`; equity avg `0.2101` n `150`; fx avg `0.0271` n `6`; index avg `0.0527` n `26`; metal avg `0.0726` n `20`; unknown avg `-0.4997` n `999`
- 24h: commodity avg `0.3704` n `13`; crypto_alt avg `-3.3899` n `235`; crypto_major avg `-3.1311` n `8`; equity avg `-1.2632` n `150`; fx avg `-0.1487` n `6`; index avg `-0.1826` n `26`; metal avg `-0.6786` n `20`; unknown avg `247.6064` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
