# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T06:22:26.480979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3239` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.2676` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.2047` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.0768` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0155` n `13`; crypto_alt avg `0.0819` n `239`; crypto_major avg `0.2372` n `8`; equity avg `0.042` n `166`; fx avg `-0.0064` n `6`; index avg `0.0025` n `27`; metal avg `0.0325` n `20`; unknown avg `0.0826` n `1262`
- 1h: commodity avg `0.0132` n `13`; crypto_alt avg `-0.5779` n `239`; crypto_major avg `-0.6716` n `8`; equity avg `-0.0381` n `166`; fx avg `-0.0028` n `6`; index avg `0.0026` n `27`; metal avg `0.0036` n `20`; unknown avg `164.2392` n `1232`
- 4h: commodity avg `-0.0299` n `13`; crypto_alt avg `-3.9281` n `239`; crypto_major avg `-4.3538` n `8`; equity avg `-1.277` n `166`; fx avg `-0.0224` n `6`; index avg `-0.0862` n `27`; metal avg `-0.1491` n `20`; unknown avg `33.3964` n `1220`
- 24h: commodity avg `0.2832` n `13`; crypto_alt avg `-7.4834` n `239`; crypto_major avg `-9.3232` n `8`; equity avg `-5.7607` n `166`; fx avg `-0.0882` n `6`; index avg `-0.5991` n `27`; metal avg `-0.4242` n `20`; unknown avg `17.2147` n `1109`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
