# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T12:07:24.544415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0638` n `13`; crypto_alt avg `-0.059` n `239`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0425` n `160`; fx avg `0.0114` n `6`; index avg `0.0014` n `27`; metal avg `0.0626` n `20`; unknown avg `0.6665` n `1252`
- 1h: commodity avg `-0.0817` n `13`; crypto_alt avg `0.0757` n `239`; crypto_major avg `0.0101` n `8`; equity avg `0.0393` n `160`; fx avg `-0.0051` n `6`; index avg `0.0003` n `27`; metal avg `0.032` n `20`; unknown avg `0.4787` n `1250`
- 4h: commodity avg `-0.0774` n `13`; crypto_alt avg `-0.3957` n `239`; crypto_major avg `-0.8438` n `8`; equity avg `-0.6519` n `160`; fx avg `0.0035` n `6`; index avg `-0.0611` n `27`; metal avg `-0.18` n `20`; unknown avg `19.0407` n `1229`
- 24h: commodity avg `-0.3256` n `13`; crypto_alt avg `0.0919` n `239`; crypto_major avg `-0.3976` n `8`; equity avg `3.4768` n `160`; fx avg `-0.001` n `6`; index avg `0.4087` n `27`; metal avg `-0.0415` n `20`; unknown avg `4.7681` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2351`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
