# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T12:22:24.428730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.1574` n `236`; crypto_major avg `-0.1365` n `8`; equity avg `0.0017` n `151`; fx avg `0.0008` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.2079` n `1193`
- 1h: commodity avg `0.012` n `13`; crypto_alt avg `-0.4383` n `236`; crypto_major avg `-0.3434` n `8`; equity avg `-0.0935` n `151`; fx avg `0.0061` n `6`; index avg `-0.0459` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.1969` n `1185`
- 4h: commodity avg `0.0691` n `13`; crypto_alt avg `-0.8188` n `236`; crypto_major avg `-0.6254` n `8`; equity avg `-0.048` n `151`; fx avg `0.001` n `6`; index avg `-0.0083` n `26`; metal avg `0.0023` n `20`; unknown avg `0.2864` n `1183`
- 24h: commodity avg `0.4487` n `13`; crypto_alt avg `-3.0988` n `236`; crypto_major avg `-1.9879` n `8`; equity avg `-3.4195` n `151`; fx avg `0.0175` n `6`; index avg `-0.5784` n `26`; metal avg `-0.2123` n `20`; unknown avg `8.9347` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1817`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1474`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0641`, n `666`, weak_sample_signal
