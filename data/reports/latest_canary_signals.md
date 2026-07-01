# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T09:22:27.840128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0408` n `12`; crypto_alt avg `-0.0497` n `228`; crypto_major avg `-0.1422` n `8`; equity avg `-0.0555` n `88`; fx avg `0.003` n `6`; index avg `-0.0045` n `23`; metal avg `0.0793` n `20`; unknown avg `0.3966` n `765`
- 1h: commodity avg `-0.1572` n `12`; crypto_alt avg `0.5833` n `228`; crypto_major avg `0.4958` n `8`; equity avg `0.0107` n `88`; fx avg `0.008` n `6`; index avg `0.0046` n `23`; metal avg `-0.0101` n `20`; unknown avg `0.4258` n `765`
- 4h: commodity avg `-0.3746` n `12`; crypto_alt avg `-0.4629` n `228`; crypto_major avg `-0.7802` n `8`; equity avg `-0.2637` n `88`; fx avg `0.0224` n `6`; index avg `-0.0389` n `23`; metal avg `0.0282` n `20`; unknown avg `0.2795` n `743`
- 24h: commodity avg `-0.4448` n `12`; crypto_alt avg `-0.066` n `228`; crypto_major avg `-0.2686` n `8`; equity avg `0.5286` n `88`; fx avg `0.1032` n `6`; index avg `-0.0019` n `23`; metal avg `-0.6495` n `20`; unknown avg `0.463` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
