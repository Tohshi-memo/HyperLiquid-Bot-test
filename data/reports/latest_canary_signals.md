# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T03:08:07.676663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0356` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7941` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6592` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.0908` n `235`; crypto_major avg `0.1554` n `8`; equity avg `-0.0059` n `150`; fx avg `0.0058` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0233` n `20`; unknown avg `0.2591` n `1074`
- 1h: commodity avg `0.0144` n `13`; crypto_alt avg `0.5389` n `235`; crypto_major avg `0.509` n `8`; equity avg `0.2012` n `150`; fx avg `0.0039` n `6`; index avg `0.0277` n `26`; metal avg `0.0042` n `20`; unknown avg `2.9099` n `1074`
- 4h: commodity avg `0.1897` n `13`; crypto_alt avg `-2.7646` n `235`; crypto_major avg `-1.8459` n `8`; equity avg `-0.564` n `150`; fx avg `-0.0108` n `6`; index avg `-0.0518` n `26`; metal avg `-0.1867` n `20`; unknown avg `1.7675` n `1068`
- 24h: commodity avg `0.4558` n `13`; crypto_alt avg `-2.7408` n `235`; crypto_major avg `-2.316` n `8`; equity avg `-0.0065` n `149`; fx avg `0.0644` n `6`; index avg `0.004` n `26`; metal avg `-0.0908` n `20`; unknown avg `871.0685` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
