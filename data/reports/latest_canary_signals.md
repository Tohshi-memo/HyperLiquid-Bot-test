# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T07:52:17.732344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7388` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1118` n `12`; crypto_alt avg `-0.0401` n `228`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0535` n `67`; fx avg `-0.0028` n `6`; index avg `-0.0444` n `23`; metal avg `-0.17` n `18`; unknown avg `-0.019` n `418`
- 1h: commodity avg `0.0719` n `12`; crypto_alt avg `-0.165` n `228`; crypto_major avg `-0.0671` n `8`; equity avg `0.1452` n `67`; fx avg `0.0066` n `6`; index avg `0.0328` n `23`; metal avg `-0.3332` n `18`; unknown avg `-0.2127` n `418`
- 4h: commodity avg `-0.362` n `12`; crypto_alt avg `0.5292` n `228`; crypto_major avg `0.7083` n `8`; equity avg `-0.0095` n `67`; fx avg `0.0343` n `6`; index avg `-0.1911` n `23`; metal avg `-1.0305` n `18`; unknown avg `0.2024` n `400`
- 24h: commodity avg `-1.0566` n `12`; crypto_alt avg `-0.7` n `228`; crypto_major avg `0.0581` n `8`; equity avg `0.8288` n `67`; fx avg `-0.0003` n `6`; index avg `0.7739` n `23`; metal avg `-1.0625` n `18`; unknown avg `0.672` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
