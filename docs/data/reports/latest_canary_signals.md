# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T07:37:24.083473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6047` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3645` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `1.4855` n `228`; crypto_major avg `1.6094` n `8`; equity avg `0.3707` n `74`; fx avg `-0.0113` n `6`; index avg `0.026` n `23`; metal avg `0.0195` n `18`; unknown avg `0.6037` n `424`
- 1h: commodity avg `-0.3173` n `12`; crypto_alt avg `0.9665` n `228`; crypto_major avg `1.1999` n `8`; equity avg `0.2523` n `74`; fx avg `0.0381` n `6`; index avg `-0.0895` n `23`; metal avg `0.2333` n `18`; unknown avg `1.093` n `424`
- 4h: commodity avg `-0.3948` n `12`; crypto_alt avg `-2.0046` n `228`; crypto_major avg `-1.43` n `8`; equity avg `-0.2923` n `74`; fx avg `-0.0014` n `6`; index avg `-0.0655` n `23`; metal avg `0.1747` n `18`; unknown avg `-0.2131` n `404`
- 24h: commodity avg `-0.5096` n `12`; crypto_alt avg `-5.9746` n `228`; crypto_major avg `-4.3601` n `8`; equity avg `-1.8866` n `73`; fx avg `0.1189` n `6`; index avg `-0.628` n `23`; metal avg `-0.2677` n `18`; unknown avg `-1.063` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
