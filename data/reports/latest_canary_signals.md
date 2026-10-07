# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T02:37:32.858403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2349` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9873` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8921` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5705` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `0.2343` n `235`; crypto_major avg `0.1174` n `8`; equity avg `0.1837` n `150`; fx avg `-0.0134` n `6`; index avg `0.0381` n `26`; metal avg `0.0321` n `20`; unknown avg `0.3895` n `1076`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `-2.0087` n `235`; crypto_major avg `-1.6136` n `8`; equity avg `-0.3918` n `150`; fx avg `-0.0072` n `6`; index avg `-0.0431` n `26`; metal avg `-0.1174` n `20`; unknown avg `0.7883` n `1074`
- 4h: commodity avg `0.1987` n `13`; crypto_alt avg `-2.5764` n `235`; crypto_major avg `-2.0362` n `8`; equity avg `-0.6073` n `150`; fx avg `-0.0051` n `6`; index avg `-0.0489` n `26`; metal avg `-0.1441` n `20`; unknown avg `2.0911` n `1068`
- 24h: commodity avg `0.4365` n `13`; crypto_alt avg `-2.7242` n `235`; crypto_major avg `-2.4968` n `8`; equity avg `-0.0087` n `149`; fx avg `0.0789` n `6`; index avg `0.0039` n `26`; metal avg `-0.0062` n `20`; unknown avg `871.2875` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
