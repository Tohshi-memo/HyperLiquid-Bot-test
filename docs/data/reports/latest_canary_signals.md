# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T01:37:31.805862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `13`; crypto_alt avg `-0.4532` n `237`; crypto_major avg `-0.4024` n `8`; equity avg `-0.2752` n `151`; fx avg `0.0051` n `6`; index avg `-0.0412` n `26`; metal avg `0.0067` n `20`; unknown avg `0.4439` n `1201`
- 1h: commodity avg `0.107` n `13`; crypto_alt avg `-0.4667` n `237`; crypto_major avg `-0.6376` n `8`; equity avg `-0.4921` n `151`; fx avg `0.0038` n `6`; index avg `-0.0687` n `26`; metal avg `-0.2212` n `20`; unknown avg `0.1958` n `1193`
- 4h: commodity avg `0.1853` n `13`; crypto_alt avg `-1.094` n `237`; crypto_major avg `-1.1497` n `8`; equity avg `-1.4693` n `151`; fx avg `-0.0197` n `6`; index avg `-0.2275` n `26`; metal avg `-0.2299` n `20`; unknown avg `1.4546` n `1042`
- 24h: commodity avg `-0.5525` n `13`; crypto_alt avg `1.0686` n `237`; crypto_major avg `0.4689` n `8`; equity avg `-1.3389` n `151`; fx avg `-0.0085` n `6`; index avg `-0.1845` n `26`; metal avg `-0.3762` n `20`; unknown avg `117.2965` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.166`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0896`, n `669`, weak_sample_signal
