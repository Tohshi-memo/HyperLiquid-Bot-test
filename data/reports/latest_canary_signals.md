# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T13:22:22.771272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.0766` n `231`; crypto_major avg `-0.0194` n `8`; equity avg `-0.0194` n `128`; fx avg `0.0007` n `6`; index avg `0.0008` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.1521` n `793`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `0.2437` n `231`; crypto_major avg `0.2308` n `8`; equity avg `-0.0394` n `128`; fx avg `0.0021` n `6`; index avg `0.0207` n `26`; metal avg `0.0239` n `20`; unknown avg `-0.0245` n `793`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `1.0204` n `231`; crypto_major avg `0.5945` n `8`; equity avg `-0.0108` n `128`; fx avg `0.0018` n `6`; index avg `0.0298` n `26`; metal avg `0.0121` n `20`; unknown avg `-0.0444` n `789`
- 24h: commodity avg `-0.0234` n `12`; crypto_alt avg `1.8426` n `231`; crypto_major avg `1.2964` n `8`; equity avg `0.2739` n `128`; fx avg `0.0175` n `6`; index avg `0.0724` n `26`; metal avg `0.0794` n `20`; unknown avg `-0.049` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
