# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T22:07:25.744202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.5291` n `234`; crypto_major avg `0.4946` n `8`; equity avg `0.0815` n `141`; fx avg `0.0049` n `6`; index avg `0.038` n `26`; metal avg `0.0024` n `20`; unknown avg `0.3475` n `943`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `0.8525` n `234`; crypto_major avg `0.8784` n `8`; equity avg `0.1316` n `141`; fx avg `0.005` n `6`; index avg `0.0343` n `26`; metal avg `0.0238` n `20`; unknown avg `0.3752` n `927`
- 4h: commodity avg `0.2215` n `12`; crypto_alt avg `-0.0495` n `234`; crypto_major avg `0.679` n `8`; equity avg `-0.1109` n `141`; fx avg `-0.0191` n `6`; index avg `0.0262` n `26`; metal avg `0.0185` n `20`; unknown avg `1.1283` n `845`
- 24h: commodity avg `0.5671` n `12`; crypto_alt avg `-3.0744` n `234`; crypto_major avg `-2.6294` n `8`; equity avg `-1.5183` n `140`; fx avg `0.0083` n `6`; index avg `-0.3204` n `26`; metal avg `-0.7965` n `20`; unknown avg `583.4465` n `821`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
