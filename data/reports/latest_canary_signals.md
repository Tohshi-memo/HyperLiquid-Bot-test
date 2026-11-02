# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T23:37:31.174680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `13`; crypto_alt avg `0.0297` n `239`; crypto_major avg `0.0232` n `8`; equity avg `-0.0376` n `157`; fx avg `0.0014` n `6`; index avg `0.0142` n `27`; metal avg `-0.0122` n `20`; unknown avg `158.15` n `1264`
- 1h: commodity avg `-0.0235` n `13`; crypto_alt avg `0.1189` n `239`; crypto_major avg `0.1396` n `8`; equity avg `0.6249` n `157`; fx avg `-0.0077` n `6`; index avg `0.1276` n `27`; metal avg `-0.0139` n `20`; unknown avg `0.2466` n `1250`
- 4h: commodity avg `-0.0581` n `13`; crypto_alt avg `0.5751` n `239`; crypto_major avg `0.5703` n `8`; equity avg `0.2989` n `157`; fx avg `-0.0178` n `6`; index avg `0.0522` n `27`; metal avg `0.0136` n `20`; unknown avg `14.0572` n `1144`
- 24h: commodity avg `-1.3408` n `13`; crypto_alt avg `-2.8873` n `238`; crypto_major avg `-1.6044` n `8`; equity avg `-2.6519` n `157`; fx avg `0.239` n `6`; index avg `0.065` n `27`; metal avg `0.102` n `20`; unknown avg `12.9057` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
