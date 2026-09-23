# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T23:52:30.532741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.1868` n `234`; crypto_major avg `0.0757` n `8`; equity avg `-0.0088` n `141`; fx avg `-0.0042` n `6`; index avg `-0.0149` n `26`; metal avg `0.0244` n `20`; unknown avg `0.6795` n `945`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.0109` n `234`; crypto_major avg `-0.15` n `8`; equity avg `-0.0888` n `141`; fx avg `-0.0164` n `6`; index avg `-0.032` n `26`; metal avg `-0.0238` n `20`; unknown avg `-0.2665` n `943`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.0082` n `234`; crypto_major avg `0.1484` n `8`; equity avg `0.132` n `141`; fx avg `-0.0275` n `6`; index avg `0.0139` n `26`; metal avg `0.0345` n `20`; unknown avg `-0.9482` n `845`
- 24h: commodity avg `0.4939` n `12`; crypto_alt avg `-4.5824` n `234`; crypto_major avg `-3.3122` n `8`; equity avg `-1.748` n `140`; fx avg `0.0393` n `6`; index avg `-0.395` n `26`; metal avg `-0.8498` n `20`; unknown avg `584.2832` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
