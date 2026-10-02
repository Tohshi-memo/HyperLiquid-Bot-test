# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T17:52:28.144440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0699` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7002` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.031` n `13`; crypto_alt avg `-0.0334` n `235`; crypto_major avg `0.0802` n `8`; equity avg `0.1576` n `143`; fx avg `-0.0043` n `6`; index avg `0.0213` n `26`; metal avg `0.0202` n `20`; unknown avg `-0.1133` n `984`
- 1h: commodity avg `0.0562` n `13`; crypto_alt avg `-0.6466` n `235`; crypto_major avg `-0.2407` n `8`; equity avg `0.0651` n `143`; fx avg `0.0004` n `6`; index avg `-0.007` n `26`; metal avg `0.0124` n `20`; unknown avg `0.3068` n `982`
- 4h: commodity avg `0.2822` n `13`; crypto_alt avg `-1.886` n `235`; crypto_major avg `-1.7877` n `8`; equity avg `-0.3958` n `143`; fx avg `0.0138` n `6`; index avg `-0.0875` n `26`; metal avg `-0.4276` n `20`; unknown avg `2.1475` n `934`
- 24h: commodity avg `-0.0792` n `13`; crypto_alt avg `0.3573` n `235`; crypto_major avg `0.0153` n `8`; equity avg `0.5625` n `142`; fx avg `-0.0797` n `6`; index avg `0.2653` n `26`; metal avg `-0.3072` n `20`; unknown avg `99.585` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
