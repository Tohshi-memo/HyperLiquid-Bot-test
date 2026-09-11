# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T16:22:27.555551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.3` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.171` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0922` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8537` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.331` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0588` n `12`; crypto_alt avg `-0.4871` n `233`; crypto_major avg `-0.5874` n `8`; equity avg `-0.2462` n `136`; fx avg `-0.0058` n `6`; index avg `-0.0348` n `26`; metal avg `-0.0729` n `20`; unknown avg `0.4542` n `796`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-1.1624` n `233`; crypto_major avg `-1.3585` n `8`; equity avg `-0.1931` n `136`; fx avg `0.0064` n `6`; index avg `-0.0275` n `26`; metal avg `-0.0865` n `20`; unknown avg `1.7209` n `794`
- 4h: commodity avg `0.1471` n `12`; crypto_alt avg `2.5266` n `233`; crypto_major avg `2.2393` n `8`; equity avg `0.3856` n `136`; fx avg `-0.0339` n `6`; index avg `0.0832` n `26`; metal avg `0.0683` n `20`; unknown avg `0.7203` n `772`
- 24h: commodity avg `-0.373` n `12`; crypto_alt avg `1.8146` n `233`; crypto_major avg `2.2121` n `8`; equity avg `0.3667` n `136`; fx avg `-0.1598` n `6`; index avg `0.3002` n `26`; metal avg `0.0421` n `20`; unknown avg `2.3153` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
