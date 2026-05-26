# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T19:22:21.072302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8381` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7611` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0946` n `12`; crypto_alt avg `-0.2055` n `228`; crypto_major avg `-0.1469` n `8`; equity avg `-0.0367` n `67`; fx avg `0.0045` n `6`; index avg `0.0459` n `23`; metal avg `0.1573` n `18`; unknown avg `-0.2356` n `418`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `-0.7901` n `228`; crypto_major avg `-0.7186` n `8`; equity avg `-0.3586` n `67`; fx avg `0.0133` n `6`; index avg `0.0303` n `23`; metal avg `0.4212` n `18`; unknown avg `-0.2403` n `418`
- 4h: commodity avg `-0.4755` n `12`; crypto_alt avg `-1.7579` n `228`; crypto_major avg `-1.5811` n `8`; equity avg `-0.1583` n `67`; fx avg `0.0479` n `6`; index avg `0.18` n `23`; metal avg `0.257` n `18`; unknown avg `0.5063` n `418`
- 24h: commodity avg `1.001` n `12`; crypto_alt avg `-2.7376` n `228`; crypto_major avg `-1.9469` n `8`; equity avg `-0.512` n `67`; fx avg `-0.1061` n `6`; index avg `0.4494` n `23`; metal avg `-0.9982` n `18`; unknown avg `-0.4349` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
