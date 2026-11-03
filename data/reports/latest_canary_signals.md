# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T14:22:32.837297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.106` n `13`; crypto_alt avg `0.068` n `239`; crypto_major avg `0.1666` n `8`; equity avg `-0.0769` n `157`; fx avg `0.0033` n `6`; index avg `-0.0133` n `27`; metal avg `-0.0019` n `20`; unknown avg `1.2136` n `1264`
- 1h: commodity avg `-0.3564` n `13`; crypto_alt avg `0.1463` n `239`; crypto_major avg `0.3041` n `8`; equity avg `0.3242` n `157`; fx avg `-0.0124` n `6`; index avg `0.069` n `27`; metal avg `0.1491` n `20`; unknown avg `38.8681` n `1256`
- 4h: commodity avg `-0.5425` n `13`; crypto_alt avg `1.127` n `239`; crypto_major avg `0.8916` n `8`; equity avg `0.5806` n `157`; fx avg `-0.0022` n `6`; index avg `0.0912` n `27`; metal avg `0.3689` n `20`; unknown avg `282.2731` n `1222`
- 24h: commodity avg `-0.6021` n `13`; crypto_alt avg `-0.648` n `239`; crypto_major avg `-0.1049` n `8`; equity avg `-2.4286` n `157`; fx avg `0.0125` n `6`; index avg `-0.1476` n `27`; metal avg `-0.2405` n `20`; unknown avg `-0.0398` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
