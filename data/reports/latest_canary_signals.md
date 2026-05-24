# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T08:22:15.480072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.2086` n `228`; crypto_major avg `0.1505` n `8`; equity avg `0.0556` n `67`; fx avg `0.0012` n `6`; index avg `0.0179` n `23`; metal avg `0.0153` n `18`; unknown avg `1.1073` n `396`
- 1h: commodity avg `-0.1962` n `12`; crypto_alt avg `0.0324` n `228`; crypto_major avg `0.0721` n `8`; equity avg `-0.0063` n `67`; fx avg `-0.0006` n `6`; index avg `-0.0285` n `23`; metal avg `0.1298` n `18`; unknown avg `1.0669` n `396`
- 4h: commodity avg `0.1457` n `12`; crypto_alt avg `-0.1066` n `228`; crypto_major avg `0.4108` n `8`; equity avg `0.1181` n `67`; fx avg `0.0128` n `6`; index avg `-0.0013` n `23`; metal avg `0.1277` n `18`; unknown avg `1.051` n `386`
- 24h: commodity avg `-2.8108` n `12`; crypto_alt avg `4.0464` n `228`; crypto_major avg `4.2162` n `8`; equity avg `2.7491` n `67`; fx avg `0.0706` n `6`; index avg `1.3603` n `23`; metal avg `1.3192` n `18`; unknown avg `3.323` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
