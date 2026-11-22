# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T04:22:35.236631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2911` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `0.0106` n `239`; crypto_major avg `-0.1192` n `8`; equity avg `-0.0528` n `166`; fx avg `-0.0009` n `6`; index avg `-0.0047` n `27`; metal avg `0.0023` n `20`; unknown avg `7.336` n `1259`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `0.1211` n `239`; crypto_major avg `-0.0773` n `8`; equity avg `-0.0941` n `166`; fx avg `0.0057` n `6`; index avg `0.0082` n `27`; metal avg `-0.0029` n `20`; unknown avg `605.5724` n `1255`
- 4h: commodity avg `-0.0964` n `13`; crypto_alt avg `-0.9386` n `239`; crypto_major avg `-1.3761` n `8`; equity avg `-0.5062` n `166`; fx avg `0.0015` n `6`; index avg `-0.085` n `27`; metal avg `-0.1126` n `20`; unknown avg `6.566` n `1257`
- 24h: commodity avg `-0.0108` n `13`; crypto_alt avg `3.8012` n `239`; crypto_major avg `5.6138` n `8`; equity avg `1.8709` n `166`; fx avg `-0.0241` n `6`; index avg `0.2478` n `27`; metal avg `0.2223` n `20`; unknown avg `946.5925` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
