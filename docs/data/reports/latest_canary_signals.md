# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T10:22:28.978377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `-0.3412` n `239`; crypto_major avg `-0.1084` n `8`; equity avg `-0.0114` n `162`; fx avg `-0.0031` n `6`; index avg `-0.006` n `27`; metal avg `-0.0059` n `20`; unknown avg `-0.0586` n `1256`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.0476` n `239`; crypto_major avg `0.332` n `8`; equity avg `0.0757` n `162`; fx avg `0.0002` n `6`; index avg `0.0121` n `27`; metal avg `0.0142` n `20`; unknown avg `4.9852` n `1242`
- 4h: commodity avg `-0.002` n `13`; crypto_alt avg `-1.4499` n `239`; crypto_major avg `-0.4673` n `8`; equity avg `-0.0039` n `162`; fx avg `-0.0101` n `6`; index avg `-0.0041` n `27`; metal avg `0.0292` n `20`; unknown avg `6.6867` n `1174`
- 24h: commodity avg `-0.0786` n `13`; crypto_alt avg `-3.0475` n `239`; crypto_major avg `-3.2687` n `8`; equity avg `-2.7901` n `162`; fx avg `-0.129` n `6`; index avg `-0.2349` n `27`; metal avg `-0.3358` n `20`; unknown avg `4.4034` n `1074`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
