# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T23:07:29.243433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0232` n `235`; crypto_major avg `0.0196` n `8`; equity avg `-0.0145` n `150`; fx avg `0.0048` n `6`; index avg `-0.0081` n `26`; metal avg `0.0068` n `20`; unknown avg `0.117` n `1075`
- 1h: commodity avg `-0.0765` n `13`; crypto_alt avg `0.096` n `235`; crypto_major avg `0.0561` n `8`; equity avg `0.047` n `150`; fx avg `0.0117` n `6`; index avg `0.0162` n `26`; metal avg `0.0517` n `20`; unknown avg `-0.2025` n `1075`
- 4h: commodity avg `-0.1885` n `13`; crypto_alt avg `1.3097` n `235`; crypto_major avg `1.096` n `8`; equity avg `0.6789` n `150`; fx avg `0.0211` n `6`; index avg `0.0921` n `26`; metal avg `0.0769` n `20`; unknown avg `0.2675` n `1007`
- 24h: commodity avg `0.488` n `13`; crypto_alt avg `-2.8744` n `235`; crypto_major avg `-3.2579` n `8`; equity avg `-2.7554` n `150`; fx avg `0.063` n `6`; index avg `-0.3606` n `26`; metal avg `0.0403` n `20`; unknown avg `6.3798` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
