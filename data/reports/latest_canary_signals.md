# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T03:07:25.718388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.112` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `0.325` n `239`; crypto_major avg `0.4119` n `8`; equity avg `0.0648` n `168`; fx avg `0.0111` n `6`; index avg `0.0033` n `27`; metal avg `0.0686` n `20`; unknown avg `0.1767` n `1259`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.7272` n `239`; crypto_major avg `0.8537` n `8`; equity avg `0.7504` n `168`; fx avg `0.028` n `6`; index avg `0.0602` n `27`; metal avg `0.1357` n `20`; unknown avg `0.31` n `1253`
- 4h: commodity avg `0.1575` n `13`; crypto_alt avg `1.8222` n `239`; crypto_major avg `2.2695` n `8`; equity avg `2.3792` n `168`; fx avg `0.0337` n `6`; index avg `0.2258` n `27`; metal avg `0.9916` n `20`; unknown avg `1.2453` n `1245`
- 24h: commodity avg `0.2452` n `13`; crypto_alt avg `1.6873` n `239`; crypto_major avg `1.836` n `8`; equity avg `1.9825` n `168`; fx avg `0.057` n `6`; index avg `0.1943` n `27`; metal avg `0.7373` n `20`; unknown avg `182.2693` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
