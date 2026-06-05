# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T10:37:24.104017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0966` n `12`; crypto_alt avg `0.0423` n `228`; crypto_major avg `-0.1217` n `8`; equity avg `0.0816` n `74`; fx avg `0.0097` n `6`; index avg `0.0567` n `23`; metal avg `-0.0626` n `18`; unknown avg `-0.2336` n `424`
- 1h: commodity avg `-0.1072` n `12`; crypto_alt avg `-0.0788` n `228`; crypto_major avg `-0.2977` n `8`; equity avg `0.2696` n `74`; fx avg `0.033` n `6`; index avg `0.0462` n `23`; metal avg `0.1576` n `18`; unknown avg `0.4002` n `424`
- 4h: commodity avg `-0.2953` n `12`; crypto_alt avg `1.2901` n `228`; crypto_major avg `1.207` n `8`; equity avg `0.9749` n `74`; fx avg `0.0883` n `6`; index avg `0.1545` n `23`; metal avg `0.3807` n `18`; unknown avg `1.3028` n `424`
- 24h: commodity avg `-0.6011` n `12`; crypto_alt avg `-3.7983` n `228`; crypto_major avg `-2.7886` n `8`; equity avg `0.0999` n `73`; fx avg `0.1191` n `6`; index avg `0.1132` n `23`; metal avg `-0.3608` n `18`; unknown avg `0.2809` n `402`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
