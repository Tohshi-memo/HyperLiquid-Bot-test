# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T15:37:26.974952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2191` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3711` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0464` n `13`; crypto_alt avg `-0.4606` n `239`; crypto_major avg `-0.5738` n `8`; equity avg `-0.1371` n `162`; fx avg `-0.0077` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0224` n `20`; unknown avg `0.0852` n `1262`
- 1h: commodity avg `-0.095` n `13`; crypto_alt avg `-1.3785` n `239`; crypto_major avg `-1.577` n `8`; equity avg `-2.2631` n `162`; fx avg `-0.0116` n `6`; index avg `-0.2059` n `27`; metal avg `-0.161` n `20`; unknown avg `0.9442` n `1256`
- 4h: commodity avg `-0.0583` n `13`; crypto_alt avg `-0.6238` n `239`; crypto_major avg `-1.1926` n `8`; equity avg `-3.4117` n `162`; fx avg `-0.0151` n `6`; index avg `-0.3114` n `27`; metal avg `-0.1514` n `20`; unknown avg `41.9172` n `1248`
- 24h: commodity avg `0.4359` n `13`; crypto_alt avg `0.4773` n `239`; crypto_major avg `-1.5859` n `8`; equity avg `-3.1426` n `162`; fx avg `0.0047` n `6`; index avg `-0.2606` n `27`; metal avg `-0.0112` n `20`; unknown avg `7.4741` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
