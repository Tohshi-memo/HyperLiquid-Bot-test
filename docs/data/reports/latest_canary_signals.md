# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T03:22:24.901129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.35` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.1652` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.0201` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7505` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0728` n `13`; crypto_alt avg `0.3188` n `239`; crypto_major avg `0.3905` n `8`; equity avg `0.4809` n `158`; fx avg `-0.0087` n `6`; index avg `0.0884` n `27`; metal avg `0.0734` n `20`; unknown avg `1.0216` n `1264`
- 1h: commodity avg `0.0313` n `13`; crypto_alt avg `-0.8036` n `239`; crypto_major avg `-0.6841` n `8`; equity avg `-0.7125` n `158`; fx avg `-0.0012` n `6`; index avg `-0.1147` n `27`; metal avg `-0.119` n `20`; unknown avg `1.7273` n `1258`
- 4h: commodity avg `-0.3575` n `13`; crypto_alt avg `-2.4457` n `239`; crypto_major avg `-2.3776` n `8`; equity avg `-3.5425` n `158`; fx avg `-0.0353` n `6`; index avg `-0.6271` n `27`; metal avg `-0.2124` n `20`; unknown avg `5.9222` n `1252`
- 24h: commodity avg `-0.1352` n `13`; crypto_alt avg `-0.465` n `239`; crypto_major avg `-0.815` n `8`; equity avg `-1.1898` n `158`; fx avg `0.1268` n `6`; index avg `-0.4382` n `27`; metal avg `-0.4853` n `20`; unknown avg `-0.2834` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
