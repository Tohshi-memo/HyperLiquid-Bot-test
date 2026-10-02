# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T18:07:38.042959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1566` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1135` n `13`; crypto_alt avg `-0.2619` n `235`; crypto_major avg `-0.0485` n `8`; equity avg `-0.0718` n `143`; fx avg `-0.0025` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.0635` n `982`
- 1h: commodity avg `0.1047` n `13`; crypto_alt avg `-0.7088` n `235`; crypto_major avg `-0.2138` n `8`; equity avg `-0.0272` n `143`; fx avg `0.0077` n `6`; index avg `-0.0092` n `26`; metal avg `0.0078` n `20`; unknown avg `0.818` n `982`
- 4h: commodity avg `0.6842` n `13`; crypto_alt avg `-1.8095` n `235`; crypto_major avg `-1.4724` n `8`; equity avg `-0.7761` n `143`; fx avg `-0.0055` n `6`; index avg `-0.1337` n `26`; metal avg `-0.4504` n `20`; unknown avg `1.8778` n `952`
- 24h: commodity avg `-0.2107` n `13`; crypto_alt avg `0.4244` n `235`; crypto_major avg `0.2937` n `8`; equity avg `1.0025` n `142`; fx avg `-0.1263` n `6`; index avg `0.3624` n `26`; metal avg `-0.2063` n `20`; unknown avg `100.4876` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
