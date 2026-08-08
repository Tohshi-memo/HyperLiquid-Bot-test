# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T01:22:25.674228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.0122` n `230`; crypto_major avg `0.0739` n `8`; equity avg `0.002` n `112`; fx avg `-0.0017` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.0442` n `783`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `0.1338` n `8`; equity avg `-0.0007` n `112`; fx avg `0.0007` n `6`; index avg `-0.0026` n `25`; metal avg `0.0166` n `20`; unknown avg `-0.1549` n `783`
- 4h: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `0.0653` n `8`; equity avg `0.1267` n `112`; fx avg `0.0107` n `6`; index avg `-0.0287` n `25`; metal avg `0.0921` n `20`; unknown avg `-0.2914` n `782`
- 24h: commodity avg `-0.1413` n `12`; crypto_alt avg `-0.5997` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `2.4522` n `112`; fx avg `-0.0824` n `6`; index avg `0.233` n `25`; metal avg `0.5041` n `20`; unknown avg `-0.0807` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
