# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T22:10:06.198673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.6114` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5644` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0545` n `12`; crypto_alt avg `-0.4475` n `228`; crypto_major avg `-0.2222` n `8`; equity avg `-0.1026` n `74`; fx avg `-0.0071` n `6`; index avg `-0.189` n `23`; metal avg `-0.0099` n `18`; unknown avg `-0.4823` n `424`
- 1h: commodity avg `-0.2191` n `12`; crypto_alt avg `-2.312` n `228`; crypto_major avg `-1.5991` n `8`; equity avg `-0.1896` n `74`; fx avg `-0.017` n `6`; index avg `0.0123` n `23`; metal avg `-0.0347` n `18`; unknown avg `-0.7017` n `424`
- 4h: commodity avg `0.1636` n `12`; crypto_alt avg `-2.0716` n `228`; crypto_major avg `-0.977` n `8`; equity avg `-0.9658` n `74`; fx avg `-0.0219` n `6`; index avg `-0.272` n `23`; metal avg `-0.1769` n `18`; unknown avg `-0.7876` n `424`
- 24h: commodity avg `-0.7229` n `12`; crypto_alt avg `-8.1093` n `228`; crypto_major avg `-5.5429` n `8`; equity avg `-0.5571` n `73`; fx avg `0.0633` n `6`; index avg `0.2446` n `23`; metal avg `0.897` n `18`; unknown avg `-1.0759` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
