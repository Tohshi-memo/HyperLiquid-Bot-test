# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T06:07:25.394400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0463` n `231`; crypto_major avg `0.0744` n `8`; equity avg `-0.0208` n `127`; fx avg `-0.0244` n `6`; index avg `0.0027` n `26`; metal avg `0.0351` n `20`; unknown avg `-0.0406` n `760`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.0913` n `231`; crypto_major avg `0.2383` n `8`; equity avg `-0.3278` n `127`; fx avg `-0.0416` n `6`; index avg `-0.0497` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.0087` n `760`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `-1.2018` n `231`; crypto_major avg `-0.579` n `8`; equity avg `-0.6572` n `127`; fx avg `-0.0556` n `6`; index avg `-0.0801` n `26`; metal avg `0.0671` n `20`; unknown avg `-0.2233` n `760`
- 24h: commodity avg `0.3609` n `12`; crypto_alt avg `0.7434` n `231`; crypto_major avg `1.6492` n `8`; equity avg `-0.1812` n `127`; fx avg `-0.078` n `6`; index avg `0.0654` n `26`; metal avg `0.1053` n `20`; unknown avg `0.5228` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
