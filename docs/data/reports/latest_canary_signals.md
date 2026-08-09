# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:37:26.732021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.0558` n `230`; crypto_major avg `-0.0284` n `8`; equity avg `-0.0082` n `112`; fx avg `0.0034` n `6`; index avg `-0.001` n `25`; metal avg `0.0054` n `20`; unknown avg `0.0879` n `785`
- 1h: commodity avg `-0.0361` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.0688` n `8`; equity avg `0.0304` n `112`; fx avg `0.0072` n `6`; index avg `0.012` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0615` n `785`
- 4h: commodity avg `-0.1538` n `12`; crypto_alt avg `0.4812` n `230`; crypto_major avg `0.2776` n `8`; equity avg `0.1102` n `112`; fx avg `0.0033` n `6`; index avg `0.0117` n `25`; metal avg `0.0181` n `20`; unknown avg `-0.0179` n `785`
- 24h: commodity avg `0.0886` n `12`; crypto_alt avg `0.963` n `230`; crypto_major avg `-0.1097` n `8`; equity avg `0.3299` n `112`; fx avg `-0.0042` n `6`; index avg `0.0222` n `25`; metal avg `0.0569` n `20`; unknown avg `0.3488` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
