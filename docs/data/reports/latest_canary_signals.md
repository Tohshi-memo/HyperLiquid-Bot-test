# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T19:07:26.790613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `13`; crypto_alt avg `0.0788` n `235`; crypto_major avg `0.0828` n `8`; equity avg `0.0564` n `151`; fx avg `-0.0013` n `6`; index avg `0.0044` n `26`; metal avg `-0.0156` n `20`; unknown avg `2.5031` n `1132`
- 1h: commodity avg `-0.0535` n `13`; crypto_alt avg `-0.0107` n `235`; crypto_major avg `-0.0689` n `8`; equity avg `-0.0765` n `151`; fx avg `0.0006` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0368` n `20`; unknown avg `3.0311` n `1132`
- 4h: commodity avg `-0.0256` n `13`; crypto_alt avg `-0.6567` n `235`; crypto_major avg `-0.5975` n `8`; equity avg `-0.3419` n `151`; fx avg `-0.042` n `6`; index avg `-0.032` n `26`; metal avg `-0.0331` n `20`; unknown avg `2.6262` n `1126`
- 24h: commodity avg `0.4291` n `13`; crypto_alt avg `-2.9218` n `235`; crypto_major avg `-1.9707` n `8`; equity avg `-3.5108` n `151`; fx avg `-0.1645` n `6`; index avg `-0.3502` n `26`; metal avg `-0.1819` n `20`; unknown avg `0.0728` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2131`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1807`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0994`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0829`, n `666`, weak_sample_signal
