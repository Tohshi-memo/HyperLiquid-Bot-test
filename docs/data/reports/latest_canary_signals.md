# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T04:52:26.395581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3006` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0681` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9857` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5426` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `0.1063` n `235`; crypto_major avg `0.0631` n `8`; equity avg `-0.0438` n `150`; fx avg `-0.0009` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.0842` n `1076`
- 1h: commodity avg `-0.0023` n `13`; crypto_alt avg `-0.6481` n `235`; crypto_major avg `-0.2822` n `8`; equity avg `-0.071` n `150`; fx avg `-0.0162` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0382` n `20`; unknown avg `-0.3036` n `1068`
- 4h: commodity avg `0.1468` n `13`; crypto_alt avg `-3.4696` n `235`; crypto_major avg `-2.1538` n `8`; equity avg `-0.6112` n `150`; fx avg `-0.0559` n `6`; index avg `-0.0857` n `26`; metal avg `-0.1681` n `20`; unknown avg `2.0169` n `1068`
- 24h: commodity avg `0.4474` n `13`; crypto_alt avg `-3.4748` n `235`; crypto_major avg `-2.502` n `8`; equity avg `0.0405` n `149`; fx avg `0.0197` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0064` n `20`; unknown avg `871.3044` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
