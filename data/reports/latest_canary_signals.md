# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T17:07:42.299976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3869` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `0.3627` n `239`; crypto_major avg `0.5587` n `8`; equity avg `0.8562` n `163`; fx avg `0.0043` n `6`; index avg `0.1023` n `27`; metal avg `0.076` n `20`; unknown avg `3.7035` n `1259`
- 1h: commodity avg `-0.1142` n `13`; crypto_alt avg `-0.2667` n `239`; crypto_major avg `0.0144` n `8`; equity avg `0.181` n `163`; fx avg `0.0058` n `6`; index avg `0.0333` n `27`; metal avg `-0.0189` n `20`; unknown avg `0.8142` n `1261`
- 4h: commodity avg `0.019` n `13`; crypto_alt avg `-1.6702` n `239`; crypto_major avg `-1.5988` n `8`; equity avg `-2.18` n `163`; fx avg `0.0476` n `6`; index avg `-0.2119` n `27`; metal avg `-0.1323` n `20`; unknown avg `7.9975` n `1209`
- 24h: commodity avg `-0.0206` n `13`; crypto_alt avg `-0.7176` n `239`; crypto_major avg `-0.4625` n `8`; equity avg `-2.4839` n `163`; fx avg `0.0175` n `6`; index avg `-0.3182` n `27`; metal avg `-0.0787` n `20`; unknown avg `15.3447` n `1096`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
