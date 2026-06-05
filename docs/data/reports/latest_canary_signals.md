# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T03:37:25.175153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1021` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.022` n `228`; crypto_major avg `0.0034` n `8`; equity avg `-0.0788` n `74`; fx avg `0.0093` n `6`; index avg `-0.0395` n `23`; metal avg `0.1508` n `18`; unknown avg `0.9101` n `424`
- 1h: commodity avg `-0.0558` n `12`; crypto_alt avg `-1.201` n `228`; crypto_major avg `-0.8872` n `8`; equity avg `-0.4029` n `74`; fx avg `0.0021` n `6`; index avg `-0.2237` n `23`; metal avg `-0.0183` n `18`; unknown avg `-0.3741` n `424`
- 4h: commodity avg `0.0397` n `12`; crypto_alt avg `-2.2076` n `228`; crypto_major avg `-1.7028` n `8`; equity avg `-0.6895` n `74`; fx avg `0.1331` n `6`; index avg `-0.6007` n `23`; metal avg `-0.7952` n `18`; unknown avg `1.1401` n `424`
- 24h: commodity avg `-0.1354` n `12`; crypto_alt avg `-6.3787` n `228`; crypto_major avg `-5.0709` n `8`; equity avg `-1.6268` n `73`; fx avg `0.2057` n `6`; index avg `-0.526` n `23`; metal avg `-0.53` n `18`; unknown avg `-0.4166` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
