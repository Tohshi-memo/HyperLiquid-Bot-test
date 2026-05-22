# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T20:37:21.767799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5785` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5101` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1265` n `12`; crypto_alt avg `-0.0392` n `228`; crypto_major avg `0.0536` n `8`; equity avg `0.007` n `67`; fx avg `-0.0109` n `6`; index avg `-0.0702` n `23`; metal avg `-0.0327` n `18`; unknown avg `-0.0579` n `386`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `0.0202` n `228`; crypto_major avg `-0.1151` n `8`; equity avg `-0.1444` n `67`; fx avg `-0.0007` n `6`; index avg `-0.0982` n `23`; metal avg `-0.0498` n `18`; unknown avg `-0.3523` n `386`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `-2.6611` n `228`; crypto_major avg `-1.826` n `8`; equity avg `-0.9306` n `67`; fx avg `0.0318` n `6`; index avg `-0.2475` n `23`; metal avg `-0.3159` n `18`; unknown avg `0.9816` n `386`
- 24h: commodity avg `-1.1077` n `12`; crypto_alt avg `-3.3267` n `228`; crypto_major avg `-2.6141` n `8`; equity avg `-1.1063` n `67`; fx avg `0.1776` n `6`; index avg `0.5168` n `23`; metal avg `-1.0187` n `18`; unknown avg `-1.4608` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
