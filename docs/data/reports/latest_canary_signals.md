# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T20:22:43.922368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1231` n `12`; crypto_alt avg `0.033` n `231`; crypto_major avg `0.0563` n `8`; equity avg `0.0439` n `122`; fx avg `0.0008` n `6`; index avg `0.0066` n `25`; metal avg `0.0146` n `20`; unknown avg `0.044` n `795`
- 1h: commodity avg `-0.4155` n `12`; crypto_alt avg `-0.6462` n `231`; crypto_major avg `-0.6634` n `8`; equity avg `0.251` n `122`; fx avg `-0.0013` n `6`; index avg `0.0624` n `25`; metal avg `0.0136` n `20`; unknown avg `-0.0047` n `795`
- 4h: commodity avg `-0.3178` n `12`; crypto_alt avg `-0.6899` n `231`; crypto_major avg `-0.3535` n `8`; equity avg `0.1279` n `122`; fx avg `0.0063` n `6`; index avg `0.036` n `25`; metal avg `0.1497` n `20`; unknown avg `-0.2934` n `795`
- 24h: commodity avg `-0.8516` n `12`; crypto_alt avg `-0.9496` n `231`; crypto_major avg `0.4461` n `8`; equity avg `2.1926` n `122`; fx avg `0.0518` n `6`; index avg `0.2693` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.4209` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
