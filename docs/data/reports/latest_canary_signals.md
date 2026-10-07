# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T07:22:32.051968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `13`; crypto_alt avg `0.0284` n `235`; crypto_major avg `0.0774` n `8`; equity avg `-0.0738` n `150`; fx avg `-0.0417` n `6`; index avg `-0.0116` n `26`; metal avg `0.017` n `20`; unknown avg `0.1445` n `1076`
- 1h: commodity avg `-0.062` n `13`; crypto_alt avg `0.3292` n `235`; crypto_major avg `0.2059` n `8`; equity avg `0.0077` n `150`; fx avg `-0.0418` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.4468` n `1074`
- 4h: commodity avg `0.0888` n `13`; crypto_alt avg `0.2917` n `235`; crypto_major avg `0.4912` n `8`; equity avg `-0.0383` n `150`; fx avg `-0.0523` n `6`; index avg `-0.0443` n `26`; metal avg `-0.0874` n `20`; unknown avg `0.3795` n `1046`
- 24h: commodity avg `0.8095` n `13`; crypto_alt avg `-2.8276` n `235`; crypto_major avg `-1.6832` n `8`; equity avg `-0.1905` n `149`; fx avg `-0.0107` n `6`; index avg `-0.0924` n `26`; metal avg `-0.1719` n `20`; unknown avg `814.2638` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
