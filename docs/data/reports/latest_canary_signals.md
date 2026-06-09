# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T02:22:23.498854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6172` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6101` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.6549` n `228`; crypto_major avg `-0.3105` n `8`; equity avg `-0.1182` n `74`; fx avg `0.0142` n `6`; index avg `-0.011` n `23`; metal avg `-0.0997` n `18`; unknown avg `-0.1502` n `517`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `-0.7719` n `228`; crypto_major avg `-0.329` n `8`; equity avg `0.1973` n `74`; fx avg `-0.0234` n `6`; index avg `0.1013` n `23`; metal avg `-0.0709` n `18`; unknown avg `-0.0469` n `517`
- 4h: commodity avg `-0.0943` n `12`; crypto_alt avg `-2.4304` n `228`; crypto_major avg `-1.6125` n `8`; equity avg `0.0047` n `74`; fx avg `-0.081` n `6`; index avg `-0.0024` n `23`; metal avg `-0.1411` n `18`; unknown avg `-0.613` n `517`
- 24h: commodity avg `-0.9451` n `12`; crypto_alt avg `-1.1507` n `228`; crypto_major avg `-0.4898` n `8`; equity avg `1.3527` n `74`; fx avg `-0.3272` n `6`; index avg `0.6243` n `23`; metal avg `0.1358` n `18`; unknown avg `-2.9557` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
