# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T05:07:24.352204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.6497` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1075` n `12`; crypto_alt avg `1.2506` n `228`; crypto_major avg `0.9273` n `8`; equity avg `0.0326` n `72`; fx avg `-0.0022` n `6`; index avg `-0.0067` n `23`; metal avg `-0.0883` n `18`; unknown avg `-0.1322` n `420`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `1.8469` n `228`; crypto_major avg `1.2677` n `8`; equity avg `0.1309` n `72`; fx avg `-0.0179` n `6`; index avg `-0.0751` n `23`; metal avg `-0.382` n `18`; unknown avg `-0.4652` n `420`
- 4h: commodity avg `-0.0628` n `12`; crypto_alt avg `1.3318` n `228`; crypto_major avg `0.4878` n `8`; equity avg `0.2382` n `72`; fx avg `-0.0053` n `6`; index avg `-0.1492` n `23`; metal avg `0.0755` n `18`; unknown avg `-0.4237` n `419`
- 24h: commodity avg `0.8988` n `12`; crypto_alt avg `-2.3154` n `228`; crypto_major avg `-4.445` n `8`; equity avg `1.0956` n `72`; fx avg `0.0322` n `6`; index avg `1.2724` n `23`; metal avg `-0.6836` n `18`; unknown avg `-0.9369` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
