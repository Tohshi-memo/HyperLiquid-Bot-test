# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T02:52:27.096359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.4407` n `234`; crypto_major avg `0.3148` n `8`; equity avg `0.0399` n `141`; fx avg `0.0039` n `6`; index avg `-0.0031` n `26`; metal avg `-0.03` n `20`; unknown avg `1.1858` n `945`
- 1h: commodity avg `-0.0748` n `12`; crypto_alt avg `1.0786` n `234`; crypto_major avg `0.5098` n `8`; equity avg `0.0466` n `141`; fx avg `0.0039` n `6`; index avg `0.0051` n `26`; metal avg `0.0027` n `20`; unknown avg `1.3611` n `943`
- 4h: commodity avg `-0.0773` n `12`; crypto_alt avg `1.0165` n `234`; crypto_major avg `0.0175` n `8`; equity avg `-0.2376` n `141`; fx avg `0.0188` n `6`; index avg `-0.0458` n `26`; metal avg `-0.058` n `20`; unknown avg `1.3753` n `937`
- 24h: commodity avg `0.4133` n `12`; crypto_alt avg `-3.7011` n `234`; crypto_major avg `-3.5653` n `8`; equity avg `-1.4777` n `140`; fx avg `0.0682` n `6`; index avg `-0.2948` n `26`; metal avg `-0.5997` n `20`; unknown avg `584.3938` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
