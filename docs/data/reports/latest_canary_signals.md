# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T20:52:30.943466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9784` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.8259` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.6716` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.8068` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.7879` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.6713` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0189` n `13`; crypto_alt avg `-2.1914` n `238`; crypto_major avg `-0.9581` n `8`; equity avg `-0.6053` n `156`; fx avg `0.0018` n `6`; index avg `-0.0337` n `27`; metal avg `-0.0671` n `20`; unknown avg `19.7105` n `1258`
- 1h: commodity avg `-0.0217` n `13`; crypto_alt avg `-4.1418` n `238`; crypto_major avg `-2.8285` n `8`; equity avg `-1.8931` n `156`; fx avg `0.0259` n `6`; index avg `-0.1572` n `27`; metal avg `-0.0406` n `20`; unknown avg `24.3679` n `1168`
- 4h: commodity avg `0.1463` n `13`; crypto_alt avg `-5.4939` n `238`; crypto_major avg `-3.8321` n `8`; equity avg `-2.3627` n `156`; fx avg `0.0175` n `6`; index avg `-0.1605` n `27`; metal avg `-0.0062` n `20`; unknown avg `30.0546` n `1170`
- 24h: commodity avg `-0.2137` n `13`; crypto_alt avg `-5.3753` n `238`; crypto_major avg `-1.81` n `8`; equity avg `-2.4866` n `155`; fx avg `0.0564` n `6`; index avg `-0.1977` n `27`; metal avg `-0.5964` n `20`; unknown avg `33.5326` n `978`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
