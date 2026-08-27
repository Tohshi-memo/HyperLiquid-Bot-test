# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T00:07:23.234769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5915` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.1844` n `231`; crypto_major avg `-0.2793` n `8`; equity avg `0.0171` n `124`; fx avg `-0.0049` n `6`; index avg `-0.0422` n `25`; metal avg `-0.0316` n `20`; unknown avg `0.523` n `795`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.6652` n `231`; crypto_major avg `0.7272` n `8`; equity avg `0.2224` n `124`; fx avg `-0.0068` n `6`; index avg `-0.0117` n `25`; metal avg `0.0253` n `20`; unknown avg `0.4948` n `795`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `2.2294` n `231`; crypto_major avg `1.7499` n `8`; equity avg `1.5966` n `124`; fx avg `-0.0257` n `6`; index avg `0.2587` n `25`; metal avg `0.1584` n `20`; unknown avg `0.7085` n `795`
- 24h: commodity avg `0.3171` n `12`; crypto_alt avg `2.1723` n `231`; crypto_major avg `1.8492` n `8`; equity avg `1.9988` n `124`; fx avg `-0.0983` n `6`; index avg `0.3993` n `25`; metal avg `-0.2215` n `20`; unknown avg `1.0569` n `778`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
