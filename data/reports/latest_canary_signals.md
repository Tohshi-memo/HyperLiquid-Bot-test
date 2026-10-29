# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T22:37:31.694020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.6877` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6244` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.456` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.2025` n `238`; crypto_major avg `0.0861` n `8`; equity avg `-0.0137` n `156`; fx avg `0.006` n `6`; index avg `-0.0049` n `27`; metal avg `0.0041` n `20`; unknown avg `159.2434` n `1258`
- 1h: commodity avg `0.0313` n `13`; crypto_alt avg `-1.1347` n `238`; crypto_major avg `-0.846` n `8`; equity avg `-0.3285` n `156`; fx avg `0.0241` n `6`; index avg `-0.0373` n `27`; metal avg `0.0152` n `20`; unknown avg `2.2105` n `1254`
- 4h: commodity avg `-0.0018` n `13`; crypto_alt avg `-4.0342` n `238`; crypto_major avg `-2.6262` n `8`; equity avg `-2.2566` n `156`; fx avg `0.0381` n `6`; index avg `-0.1702` n `27`; metal avg `0.0615` n `20`; unknown avg `22.0546` n `1162`
- 24h: commodity avg `-0.1614` n `13`; crypto_alt avg `-5.3551` n `238`; crypto_major avg `-1.7101` n `8`; equity avg `-3.1447` n `155`; fx avg `0.077` n `6`; index avg `-0.2335` n `27`; metal avg `-0.5358` n `20`; unknown avg `28.8971` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
