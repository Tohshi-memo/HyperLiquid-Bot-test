# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T13:37:12.947869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0872` n `12`; crypto_alt avg `-0.1689` n `228`; crypto_major avg `-0.1968` n `8`; equity avg `-0.0163` n `67`; fx avg `-0.0062` n `6`; index avg `0.0317` n `23`; metal avg `-0.0059` n `18`; unknown avg `0.0719` n `396`
- 1h: commodity avg `-0.0687` n `12`; crypto_alt avg `0.9159` n `228`; crypto_major avg `0.483` n `8`; equity avg `0.2578` n `67`; fx avg `-0.0006` n `6`; index avg `0.1603` n `23`; metal avg `0.0449` n `18`; unknown avg `-0.0889` n `396`
- 4h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.7453` n `228`; crypto_major avg `0.4353` n `8`; equity avg `0.2187` n `67`; fx avg `-0.0006` n `6`; index avg `0.2089` n `23`; metal avg `-0.0153` n `18`; unknown avg `-0.1775` n `396`
- 24h: commodity avg `0.4721` n `12`; crypto_alt avg `-5.4189` n `228`; crypto_major avg `-4.1039` n `8`; equity avg `-2.1133` n `67`; fx avg `0.0626` n `6`; index avg `-0.3126` n `23`; metal avg `-0.5185` n `18`; unknown avg `-2.8205` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
