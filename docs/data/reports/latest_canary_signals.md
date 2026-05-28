# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T11:07:19.219953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0437` n `12`; crypto_alt avg `-0.1254` n `228`; crypto_major avg `-0.0155` n `8`; equity avg `-0.1356` n `67`; fx avg `-0.0013` n `6`; index avg `-0.0084` n `23`; metal avg `0.0786` n `18`; unknown avg `0.847` n `419`
- 1h: commodity avg `0.3515` n `12`; crypto_alt avg `-0.8009` n `228`; crypto_major avg `-0.3616` n `8`; equity avg `-0.3852` n `67`; fx avg `-0.0214` n `6`; index avg `-0.1508` n `23`; metal avg `-0.2844` n `18`; unknown avg `1.0555` n `419`
- 4h: commodity avg `0.1019` n `12`; crypto_alt avg `-0.3989` n `228`; crypto_major avg `-0.0485` n `8`; equity avg `-0.3554` n `67`; fx avg `-0.0445` n `6`; index avg `-0.2332` n `23`; metal avg `-0.2879` n `18`; unknown avg `0.3108` n `419`
- 24h: commodity avg `0.5129` n `12`; crypto_alt avg `-5.3789` n `228`; crypto_major avg `-4.0392` n `8`; equity avg `-2.0711` n `67`; fx avg `-0.1055` n `6`; index avg `-1.3155` n `23`; metal avg `-1.2844` n `18`; unknown avg `-0.6979` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
