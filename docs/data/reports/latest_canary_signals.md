# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T08:07:18.132840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5054` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.4336` n `12`; crypto_alt avg `0.2766` n `228`; crypto_major avg `0.0135` n `8`; equity avg `0.0838` n `67`; fx avg `-0.0129` n `6`; index avg `0.0062` n `23`; metal avg `0.284` n `18`; unknown avg `0.0273` n `418`
- 1h: commodity avg `-0.2999` n `12`; crypto_alt avg `0.1662` n `228`; crypto_major avg `-0.0226` n `8`; equity avg `0.1128` n `67`; fx avg `-0.0226` n `6`; index avg `0.0062` n `23`; metal avg `-0.0197` n `18`; unknown avg `0.0203` n `418`
- 4h: commodity avg `-0.5617` n `12`; crypto_alt avg `0.9037` n `228`; crypto_major avg `0.7222` n `8`; equity avg `0.1244` n `67`; fx avg `0.0301` n `6`; index avg `-0.1616` n `23`; metal avg `-0.7832` n `18`; unknown avg `0.5066` n `400`
- 24h: commodity avg `-1.4044` n `12`; crypto_alt avg `-0.4697` n `228`; crypto_major avg `0.1529` n `8`; equity avg `0.8582` n `67`; fx avg `-0.0192` n `6`; index avg `0.788` n `23`; metal avg `-0.8098` n `18`; unknown avg `0.7149` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
