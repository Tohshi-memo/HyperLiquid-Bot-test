# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T15:22:31.994230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1728` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `-0.1392` n `233`; crypto_major avg `-0.2108` n `8`; equity avg `-0.1855` n `135`; fx avg `-0.0002` n `6`; index avg `-0.0385` n `26`; metal avg `0.0199` n `20`; unknown avg `-0.0006` n `796`
- 1h: commodity avg `0.1808` n `12`; crypto_alt avg `-0.101` n `233`; crypto_major avg `-0.1499` n `8`; equity avg `0.2031` n `135`; fx avg `0.013` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0631` n `20`; unknown avg `-0.0637` n `766`
- 4h: commodity avg `0.5277` n `12`; crypto_alt avg `-0.9705` n `233`; crypto_major avg `-1.3926` n `8`; equity avg `-0.5064` n `135`; fx avg `0.0009` n `6`; index avg `-0.2198` n `26`; metal avg `-0.3106` n `20`; unknown avg `-0.7136` n `760`
- 24h: commodity avg `0.427` n `12`; crypto_alt avg `-3.7637` n `233`; crypto_major avg `-3.0081` n `8`; equity avg `-1.516` n `135`; fx avg `0.0868` n `6`; index avg `-0.25` n `26`; metal avg `-0.8433` n `20`; unknown avg `-0.8281` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
