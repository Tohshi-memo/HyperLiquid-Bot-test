# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T18:37:24.814315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.1269` n `233`; crypto_major avg `0.0126` n `8`; equity avg `-0.0291` n `134`; fx avg `0.0029` n `6`; index avg `0.0036` n `26`; metal avg `-0.0391` n `20`; unknown avg `6.0766` n `797`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0145` n `233`; crypto_major avg `-0.1335` n `8`; equity avg `0.0446` n `134`; fx avg `-0.0262` n `6`; index avg `0.0055` n `26`; metal avg `-0.0309` n `20`; unknown avg `16.4655` n `795`
- 4h: commodity avg `-0.158` n `12`; crypto_alt avg `-0.5283` n `233`; crypto_major avg `-0.5912` n `8`; equity avg `-0.3301` n `134`; fx avg `0.0336` n `6`; index avg `-0.0839` n `26`; metal avg `-0.0807` n `20`; unknown avg `0.2322` n `789`
- 24h: commodity avg `0.179` n `12`; crypto_alt avg `-0.5338` n `233`; crypto_major avg `-0.2348` n `8`; equity avg `-0.5776` n `134`; fx avg `-0.0531` n `6`; index avg `-0.2323` n `26`; metal avg `0.4393` n `20`; unknown avg `7.944` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
