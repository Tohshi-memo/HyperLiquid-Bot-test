# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T17:07:32.525374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3757` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7547` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.065` n `13`; crypto_alt avg `-0.199` n `235`; crypto_major avg `-0.0756` n `8`; equity avg `0.0197` n `143`; fx avg `-0.0097` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.1816` n `982`
- 1h: commodity avg `0.2339` n `13`; crypto_alt avg `-0.7155` n `235`; crypto_major avg `-0.2529` n `8`; equity avg `-0.1825` n `143`; fx avg `-0.0013` n `6`; index avg `-0.0204` n `26`; metal avg `0.0526` n `20`; unknown avg `2.0852` n `982`
- 4h: commodity avg `0.536` n `13`; crypto_alt avg `-1.3632` n `235`; crypto_major avg `-1.8397` n `8`; equity avg `-0.4857` n `143`; fx avg `0.0922` n `6`; index avg `-0.085` n `26`; metal avg `-0.545` n `20`; unknown avg `1.8184` n `934`
- 24h: commodity avg `-0.1093` n `13`; crypto_alt avg `1.8807` n `235`; crypto_major avg `0.8657` n `8`; equity avg `1.3596` n `142`; fx avg `-0.0971` n `6`; index avg `0.4313` n `26`; metal avg `-0.2428` n `20`; unknown avg `101.0728` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
