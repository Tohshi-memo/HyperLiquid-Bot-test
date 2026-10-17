# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T13:52:30.880957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `0.2056` n `236`; crypto_major avg `0.1152` n `8`; equity avg `0.0313` n `151`; fx avg `-0.0021` n `6`; index avg `-0.0026` n `26`; metal avg `0.0013` n `20`; unknown avg `0.6614` n `1193`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `0.0262` n `236`; crypto_major avg `0.0738` n `8`; equity avg `0.042` n `151`; fx avg `-0.0041` n `6`; index avg `0.0025` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.1502` n `1191`
- 4h: commodity avg `0.0125` n `13`; crypto_alt avg `-1.1226` n `236`; crypto_major avg `-0.6212` n `8`; equity avg `-0.1543` n `151`; fx avg `0.0097` n `6`; index avg `-0.0376` n `26`; metal avg `-0.0057` n `20`; unknown avg `2.6299` n `1183`
- 24h: commodity avg `0.6029` n `13`; crypto_alt avg `-2.7826` n `236`; crypto_major avg `-1.3523` n `8`; equity avg `-2.122` n `151`; fx avg `-0.0047` n `6`; index avg `-0.4084` n `26`; metal avg `-0.2554` n `20`; unknown avg `10.8229` n `956`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1751`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1479`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0675`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0629`, n `666`, weak_sample_signal
